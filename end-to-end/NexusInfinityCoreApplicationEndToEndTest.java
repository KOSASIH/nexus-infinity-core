package com.nexusinfinitycore.endtoend;

import com.nexusinfinitycore.main.NexusInfinityCoreApplication;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(features = "classpath:features", glue = "com.nexusinfinitycore.endtoend.steps")
public class NexusInfinityCoreApplicationEndToEndTest {
    // No test methods needed, as Cucumber will run the feature files
}
