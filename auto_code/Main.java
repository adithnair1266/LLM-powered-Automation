import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of rows of the first matrix:");
        int m = scanner.nextInt();
        System.out.println("Enter the number of columns of the first matrix: ");
        int n = scanner.nextInt();
        System.out.println("Enter the number of rows of the second matrix:");
        int p = scanner.nextInt();
        System.out.println("Enter the number of columns of the second matrix: ");
        int q = scanner.nextInt();

        if (n != p) {
            System.out.println("Error: Number of columns of the first matrix and rows of the second matrix should be equal");
            return;
        }

        int[][] firstMatrix = new int[m][n];
        int[][] secondMatrix = new int[p][q];
        int[][] resultMatrix = new int[m][q];

        System.out.println("Enter the first matrix:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                firstMatrix[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter the second matrix:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < q; j++) {
                secondMatrix[i][j] = scanner.nextInt();
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < q; j++) {
                resultMatrix[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    resultMatrix[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
                }
            }
        }

        System.out.println("The result matrix is:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < q; j++) {
                System.out.print(resultMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}