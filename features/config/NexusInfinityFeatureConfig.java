package com.nexusinfinitycore.features.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.access.prepost.PreAuthorize;

@Configuration
public class NexusInfinityFeatureConfig {
    @PreAuthorize("hasRole('ADMIN')")
    public void configureFeatureSecurity() {
        // Implement feature-level security configuration
    }
}
