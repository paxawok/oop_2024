import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

class Length {
    private static final String DIV_BY_ZERO = "Ділення на нуль не підтримується.";
    private static final String VALUE_ERROR = "Неправильний формат даних.";


    private static List<Length> instances = new ArrayList<>();
    private static Map<String, Double> unitSymbols = new HashMap<>();

    static {
        unitSymbols.put("km", 1000.0);
        unitSymbols.put("m", 1.0);
        unitSymbols.put("dm", 0.1);
        unitSymbols.put("cm", 0.01);
        unitSymbols.put("mm", 0.001);
    }

    private double value;
    private int precision;
    private String unit;

    public Length(double value, int precision, String unit) {
        this.value = round(value, precision);
        this.precision = precision;
        this.unit = unit;
        instances.add(this);
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = round(value, precision);
    }

    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String newUnit) {
        this.unit = newUnit;
    }

    public double getDoubleValue() {
        return value * unitSymbols.get(unit);
    }

    public Length add(double other) {
        try{
            this.value += other;
            return this;
        } catch (IllegalArgumentException e) {
            System.out.println("Помилка: " + e.getMessage());
            return null;
        }
    }

    public Length multiply(double other) {
        try {
            this.value *= other;
            return this;
        } catch (IllegalArgumentException e) {
            System.out.println("Помилка: " + e.getMessage());
            return null;
        }
    }

    public Length subtract(double other) {
        try {
            this.value -= other;
            return this;
        } catch (IllegalArgumentException e) {
            System.out.println("Помилка: " + e.getMessage());
            return null;
        }
    }

    public Length divide(double other) {
        try {
            if (other == 0) {
                throw new IllegalArgumentException(Length.DIV_BY_ZERO);
            }
            this.value /= other;
            return this;
        } catch (IllegalArgumentException e) {
            System.out.println("Помилка: " + e.getMessage());
            return null;
        }
    }

    @Override
    public String toString() {
        return String.format("%." + precision + "f " + unit, value);
    }

    private double round(double value, int precision) {
        return (double) Math.round(value * Math.pow(10, precision)) / Math.pow(10, precision);
    }
    public void deleteObject() {
        try {
            instances.remove(this);
        } catch (NullPointerException e) {
            System.out.println("Помилка: " + VALUE_ERROR);
        }
    }
    public Length convert(String toUnit) {
        try {
            String fromUnit = this.getUnit();
            double factor = unitSymbols.get(fromUnit) / unitSymbols.get(toUnit);
            return new Length(this.getValue() * factor, this.getPrecision(), toUnit);
        } catch (NullPointerException e) {
            System.out.println("Помилка: " + VALUE_ERROR);
            return null;
        }
    }
    public static void printInstances() {
        System.out.println("\nІснуючі об'єкти:");

        if (instances.isEmpty()) {
            System.out.println("Пусто");
        } else {
            for (Length instance : instances) {
                System.out.println("| " + instance);
            }
        }
    }
}

