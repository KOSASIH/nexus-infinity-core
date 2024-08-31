package com.nexusinfinitycore.modules.utils;

import java.math.BigDecimal;
import java.math.MathContext;

public class MathUtils {
    /**
     * Performs a precise mathematical operation using a MathContext
     * @param operation the mathematical operation to perform
     * @param operands the operands for the operation
     * @return the result of the operation
     */
    public static BigDecimal performOperation(String operation, BigDecimal... operands) {
        MathContext mathContext = new MathContext(32); // 32-digit precision
        switch (operation) {
            case "add":
                return operands[0].add(operands[1], mathContext);
            case "subtract":
                return operands[0].subtract(operands[1], mathContext);
            case "multiply":
                return operands[0].multiply(operands[1], mathContext);
            case "divide":
                return operands[0].divide(operands[1], mathContext);
            default:
                throw new UnsupportedOperationException("Unsupported operation");
        }
    }

    /**
     * Generates a random number within a specified range
     * @param min the minimum value of the range
     * @param max the maximum value of the range
     * @return a random number within the range
     */
    public static int generateRandomNumber(int min, int max) {
        return (int) (Math.random() * (max - min + 1) + min);
    }
}
