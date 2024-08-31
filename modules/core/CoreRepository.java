package com.nexusinfinitycore.modules.core;

import com.nexusinfinitycore.modules.data.DataEntity;

import java.util.List;

public interface CoreRepository {
    /**
     * Retrieves a list of data entities
     * @return a list of data entities
     */
    List<DataEntity> getDataEntities();

    /**
     * Saves a data entity
     * @param dataEntity the data entity to save
     * @return the saved data entity
     */
    DataEntity saveDataEntity(DataEntity dataEntity);

    /**
     * Deletes a data entity
     * @param dataEntity the data entity to delete
     * @return true if deleted successfully, false otherwise
     */
    boolean deleteDataEntity(DataEntity dataEntity);
}
