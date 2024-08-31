package com.nexusinfinitycore.features.repository;

import java.util.List;

public interface NexusInfinityFeatureRepository {
    List<String> getFeatures();
    void addFeature(String feature);
    void removeFeature(String feature);
    boolean isFeatureEnabled(String feature);
    void enableFeature(String feature);
    void disableFeature(String feature);
}
