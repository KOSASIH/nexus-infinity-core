package com.nexusinfinitycore.modules.core;

import com.nexusinfinitycore.modules.data.DataService;
import com.nexusinfinitycore.modules.security.SecurityService;

import java.util.List;
import java.util.concurrent.CompletableFuture;

public interface CoreService {
    /**
     * Retrieves a welcome message for the user
     * @return a welcome message
     */
    String getWelcomeMessage();

    /**
     * Processes data using the data service and security service
     * @param dataService the data service instance
     * @param securityService the security service instance
     * @return a CompletableFuture indicating the processing result
     */
    CompletableFuture<Boolean> processData(DataService dataService, SecurityService securityService);

    /**
     * Retrieves a list of available features for the user
     * @return a list of available features
     */
    List<String> getAvailableFeatures();

    /**
     * Executes a complex business logic operation
     * @param input the input data
     * @return the result of the business logic operation
     */
    String executeBusinessLogic(String input);
}
