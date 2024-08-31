package com.nexusinfinitycore.features.service;

import java.util.List;

public interface NexusInfinityFeatureService {
    List<String> getFeatures();
    void addFeature(String feature);
    void removeFeature(String feature);
    boolean isFeatureEnabled(String feature);
    void enableFeature(String feature);
    void disableFeature(String feature);
}
