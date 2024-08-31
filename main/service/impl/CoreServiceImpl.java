package com.nexusinfinitycore.main.service.impl;

import com.nexusinfinitycore.main.repository.CoreRepository;
import com.nexusinfinitycore.main.service.CoreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CoreServiceImpl implements CoreService {
    private final CoreRepository coreRepository;

    @Autowired
    public CoreServiceImpl(CoreRepository coreRepository) {
        this.coreRepository = coreRepository;
    }

    @Override
    public List<String> getData() {
        return coreRepository.getData();
    }

    @Override
    public void storeData(String data) {
        coreRepository.storeData(data);
    }

    @Override
    public boolean authenticate(String username, String password) {
        return coreRepository.authenticate(username, password);
    }

    @Override
    public boolean authorize(String role, String resource) {
        return coreRepository.authorize(role, resource);
    }
          }
