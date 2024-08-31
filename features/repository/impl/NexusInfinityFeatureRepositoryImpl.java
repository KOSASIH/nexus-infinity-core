package com.nexusinfinitycore.features.repository.impl;

import com.nexusinfinitycore.features.repository.NexusInfinityFeatureRepository;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Repository
public class NexusInfinityFeatureRepositoryImpl implements NexusInfinityFeatureRepository {
    private Map<String, Boolean> features = new ConcurrentHashMap<>();

    @Override
    public List<String> getFeatures() {
        return new ArrayList<>(features.keySet());
    }

    @Override
    public void addFeature(String feature) {
        features.put(feature, false);
    }

    @Override
    public void removeFeature(String feature) {
        features.remove(feature);
    }

    @Override
    public boolean isFeatureEnabled(String feature) {
        return features.getOrDefault(feature, false);
    }

    @Override
    public void enableFeature(String feature) {
        features.put(feature, true);
    }

    @Override
    public void disableFeature(String feature) {
        features.put(feature, false);
    }
}
