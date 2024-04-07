import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("|-----МЕНЮ-----|\n");
        System.out.println("1 ---> Створення об'єкта");
        System.out.println("2 ---> Виведення списку об'єктів, що існують");
        System.out.println("3 ---> Операції ДВМД");
        System.out.println("4 ---> Зміна міри довжини об'єкта");
        System.out.println("5 ---> Видалення об'єктa");
        System.out.println("6 ---> Exit\n");

        while (true) {
            System.out.print("Обрати: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    System.out.println("\n1. Створюю об'єкт, вводячи всі дані з клавіатури");

                    System.out.print("Введіть довжину: ");
                    double value = scanner.nextDouble();
                    scanner.nextLine();  // Очистка буфера

                    System.out.print("Введіть кількість знаків після коми: ");
                    int precision = scanner.nextInt();
                    scanner.nextLine();  // Очистка буфера

                    System.out.println("\n km - кілометри,\n m - метри,\n dm - дециметри,\n cm - сантиметри,\n mm - міліметри,\n\nВведіть міру довжини: ");
                    String unit = scanner.nextLine();

                    Length newObject0 = new Length(value, precision, unit);
                    System.out.println(newObject0);
                    break;

                case "2":
                    Length.printInstances();
                    break;

                case "3":
                    Length length1 = new Length(13, 2, "cm");
                    Length.printInstances();
                    System.out.println("\nОперації ДВМД");

                    System.out.println("\nОперація додавання: " + length1 + " + 90 = " + length1.add(90));
                    System.out.println("\nОперація віднімання: " + length1 + " - 90 = " + length1.subtract(90));
                    System.out.println("\nОперація множення: " + length1 + " * 9 = " + length1.multiply(9));
                    System.out.println("\nОперація ділення: " + length1 + " / 90 = " + length1.divide(90));
                    System.out.println("\nOперація ділення на нуль: " + length1 + " / 0 = " + length1.divide(0));
                    Length.printInstances();
                    break;

                case "4":
                    Length length2 = new Length(71, 1, "m");
                    Length.printInstances();
                    System.out.print("\nВведіть нову міру довжини: ");
                    String newUnit = scanner.nextLine();
                    Length newObject0Unit = length2.convert(newUnit);
                    System.out.println(newObject0Unit);
                    break;

                case "5":
                    Length lengthToDelete = new Length(67, 1, "m");
                    System.out.println("\nВидалення об'єктa");
                    Length.printInstances();
                    System.out.print("\nВидалимо " + lengthToDelete + ": ");
                    lengthToDelete.deleteObject();
                    Length.printInstances();
                    break;

                case "6":
                    System.exit(0);

                default:
                    System.out.println("Невірний вибір. Спробуйте ще раз.");
                    break;
            }
        }
    }
}
