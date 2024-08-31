package com.nexusinfinitycore.modules.data;

import com.nexusinfinitycore.modules.core.CoreRepository;
import java.util.List;

public interface DataRepository extends CoreRepository {
    /**
     * Retrieves data from the database or cache
     * @return the data
     */
    String getData();

    /**
     * Saves data to the database or cache
     * @param data the data to save
     * @return true if saved successfully, false otherwise
     */
    boolean saveData(String data);

    /**
     * Executes a complex data operation
     * @param dataEntity the data entity to operate on
     * @return the result of the data operation
     */
    String executeDataOperation(DataEntity dataEntity);
}
