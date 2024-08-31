package com.nexusinfinitycore.modules.data;

import java.util.List;
import java.util.concurrent.CompletableFuture;

public interface DataService {
    /**
     * Retrieves data from the database or cache
     * @return a CompletableFuture containing the data
     */
    CompletableFuture<String> getData();

    /**
     * Saves data to the database or cache
     * @param data the data to save
     * @return a CompletableFuture indicating the save result
     */
    CompletableFuture<Boolean> saveData(String data);

    /**
     * Retrieves a list of data entities from the database or cache
     * @return a list of data entities
     */
    List<DataEntity> getDataEntities();

    /**
     * Executes a complex data operation using the data repository
     * @param dataEntity the data entity to operate on
     * @return the result of the data operation
     */
    String executeDataOperation(DataEntity dataEntity);
}
