package com.nexusinfinitycore.modules.security;

import java.util.concurrent.CompletableFuture;

public interface SecurityService {
    /**
     * Encrypts data using a secure encryption algorithm
     * @param data the data to encrypt
     * @return a CompletableFuture containing the encrypted data
     */
    CompletableFuture<String> encryptData(String data);

    /**
     * Decrypts data using a secure decryption algorithm
     * @param encryptedData the encrypted data to decrypt
     * @return a CompletableFuture containing the decrypted data
     */
    CompletableFuture<String> decryptData(String encryptedData);

    /**
     * Authenticates a user using a secure authentication mechanism
     * @param username the username to authenticate
     * @param password the password to authenticate
     * @return a CompletableFuture indicating the authentication result
     */
    CompletableFuture<Boolean> authenticateUser(String username, String password);

    /**
     * Authorizes a user to access a resource using a secure authorization mechanism
     * @param username the username to authorize
     * @param resource the resource to access
     * @return a CompletableFuture indicating the authorization result
     */
    CompletableFuture<Boolean> authorizeUser(String username, String resource);
}
