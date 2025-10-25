package com.prediction.populationhealthtrends.unwto;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class UNWTOTourismService {
    private static final String UNWTO_API_BASE = "https://api.unwto.org/v1/statistics";
    private static final List<String> NATO_COUNTRIES = Arrays.asList(
        "Albania", "Belgium", "Bulgaria", "Canada", "Croatia", "Czech Republic", "Denmark", "Estonia", "France",
        "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Montenegro",
        "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
        "Spain", "Turkey", "United Kingdom", "United States"
    );

    private final String apiKey;
    private final ObjectMapper objectMapper;

    public UNWTOTourismService(String apiKey) {
        this.apiKey = apiKey;
        this.objectMapper = new ObjectMapper();
    }

    public List<Map<String, Object>> getTourismLevels(int year) {
        List<Map<String, Object>> results = new ArrayList<>();
        for (String country : NATO_COUNTRIES) {
            String url = String.format("%s/arrivals?country=%s&year=%d", UNWTO_API_BASE, country, year);
            try {
                Map<String, Object> data = fetchData(url);
                results.add(Map.of("country", country, "data", data));
            } catch (Exception e) {
                results.add(Map.of("country", country, "error", e.getMessage()));
            }
        }
        return results;
    }

    public Map<String, Object> getCountryTourism(String country, int year) {
        if (!NATO_COUNTRIES.contains(country)) {
            return Map.of("error", "Country not in NATO list.");
        }
        String url = String.format("%s/arrivals?country=%s&year=%d", UNWTO_API_BASE, country, year);
        try {
            return fetchData(url);
        } catch (Exception e) {
            return Map.of("error", e.getMessage());
        }
    }

    private Map<String, Object> fetchData(String urlString) throws IOException {
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + apiKey);
        conn.setRequestMethod("GET");
        conn.setConnectTimeout(10000);
        conn.setReadTimeout(10000);
        int status = conn.getResponseCode();
        if (status != 200) {
            throw new IOException("HTTP error code: " + status);
        }
        return objectMapper.readValue(conn.getInputStream(), Map.class);
    }
}
