package com.nexusinfinitycore.features.service.impl;

import com.nexusinfinitycore.features.repository.NexusInfinityFeatureRepository;
import com.nexusinfinitycore.features.service.NexusInfinityFeatureService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NexusInfinityFeatureServiceImpl implements NexusInfinityFeatureService {
    private final NexusInfinityFeatureRepository featureRepository;

    @Autowired
    public NexusInfinityFeatureServiceImpl(NexusInfinityFeatureRepository featureRepository) {
        this.featureRepository = featureRepository;
    }

    @Override
    public List<String> getFeatures() {
        return featureRepository.getFeatures();
    }

    @Override
    public void addFeature(String feature) {
        featureRepository.addFeature(feature);
    }

    @Override
    public void removeFeature(String feature) {
        featureRepository.removeFeature(feature);
    }

    @Override
    public boolean isFeatureEnabled(String feature) {
        return featureRepository.isFeatureEnabled(feature);
    }

    @Override
    public void enableFeature(String feature) {
        featureRepository.enableFeature(feature);
    }

    @Override
    public void disableFeature(String feature) {
        featureRepository.disableFeature(feature);
    }
}
