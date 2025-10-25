package com.prediction.populationhealthtrends.unwto;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.io.IOException;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class UNWTOTourismServiceTest {
    private UNWTOTourismService service;
    private final String dummyApiKey = "DUMMY_KEY";

    @BeforeEach
    public void setUp() {
        service = Mockito.spy(new UNWTOTourismService(dummyApiKey));
    }

    @Test
    public void testGetCountryTourism_NonNATOCountry() {
        Map<String, Object> result = service.getCountryTourism("NonNATO", 2023);
        assertTrue(result.containsKey("error"));
        assertEquals("Country not in NATO list.", result.get("error"));
    }

    @Test
    public void testGetCountryTourism_ValidCountry() throws Exception {
        Mockito.doReturn(Map.of("arrivals", 123456)).when(service).fetchData(Mockito.anyString());
        Map<String, Object> result = service.getCountryTourism("France", 2023);
        assertTrue(result.containsKey("arrivals"));
        assertEquals(123456, result.get("arrivals"));
    }

    @Test
    public void testGetTourismLevels_AllCountries() throws Exception {
        Mockito.doReturn(Map.of("arrivals", 1000)).when(service).fetchData(Mockito.anyString());
        List<Map<String, Object>> results = service.getTourismLevels(2023);
        assertEquals(30, results.size());
        for (Map<String, Object> countryData : results) {
            assertTrue(countryData.containsKey("country"));
            assertTrue(countryData.containsKey("data"));
            assertEquals(Map.of("arrivals", 1000), countryData.get("data"));
        }
    }

    @Test
    public void testGetCountryTourism_ApiError() throws Exception {
        Mockito.doThrow(new IOException("API error")).when(service).fetchData(Mockito.anyString());
        Map<String, Object> result = service.getCountryTourism("France", 2023);
        assertTrue(result.containsKey("error"));
        assertEquals("API error", result.get("error"));
    }
}
