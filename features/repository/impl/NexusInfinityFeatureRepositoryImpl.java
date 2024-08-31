package com.nexusinfinitycore.features.repository.impl;

import com.nexusinfinitycore.features.repository.NexusInfinityFeatureRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Repository
@Transactional
public class NexusInfinityFeatureRepositoryImpl implements NexusInfinityFeatureRepository {
    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<String> getFeatures() {
        return entityManager.createQuery("SELECT f.name FROM Feature f", String.class).getResultList();
    }

    @Override
    public void addFeature(String feature) {
        Feature newFeature = new Feature(feature, false);
        entityManager.persist(newFeature);
    }

    @Override
    public void removeFeature(String feature) {
        entityManager.createQuery("DELETE FROM Feature f WHERE f.name = :feature")
                .setParameter("feature", feature)
                .executeUpdate();
    }

    @Override
    public boolean isFeatureEnabled(String feature) {
        Feature featureEntity = entityManager.find(Feature.class, feature);
        return featureEntity != null && featureEntity.isEnabled();
    }

    @Override
    public void enableFeature(String feature) {
        Feature featureEntity = entityManager.find(Feature.class, feature);
        if (featureEntity != null) {
            featureEntity.setEnabled(true);
            entityManager.merge(featureEntity);
        }
    }

    @Override
    public void disableFeature(String feature) {
        Feature featureEntity = entityManager.find(Feature.class, feature);
        if (featureEntity != null) {
            featureEntity.setEnabled(false);
            entityManager.merge(featureEntity);
        }
    }
}
