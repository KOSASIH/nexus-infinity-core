package com.nexusinfinitycore.modules.security;

import java.util.List;

public interface SecurityRepository {
    /**
     * Authenticates a user using a secure authentication mechanism
     * @param username the username to authenticate
     * @param password the password to authenticate
     * @return true if authenticated successfully, false otherwise
     */
    boolean authenticateUser(String username, String password);

    /**
     * Authorizes a user to access a resource using a secure authorization mechanism
     * @param username the username to authorize
     * @param resource the resource to access
     * @return true if authorized successfully, false otherwise
     */
    boolean authorizeUser(String username, String resource);

    /**
     * Retrieves a list of authorized resources for a user
     * @param username the username to retrieve authorized resources for
     * @return a list of authorized resources
     */
    List<String> getAuthorizedResources(String username);
}
