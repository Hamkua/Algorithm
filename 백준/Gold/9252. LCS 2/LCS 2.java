import java.io.*;
import java.util.*;

public class Main {
    static int x, y;
    static int[][] data;
    static String result = "";


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String a = br.readLine();
        String b = br.readLine();

        data = new int[a.length() + 1][b.length() + 1];
        for(int i = 0; i < a.length(); i++){
            Arrays.fill(data[i], 0);
        }

        for(int i = 1; i < a.length() + 1; i++){
            for(int j = 1; j < b.length() + 1; j++){
                if(a.charAt(i - 1) == b.charAt(j - 1)){
                    data[i][j] = data[i - 1][j - 1] + 1;
                }else{
                    data[i][j] = Math.max(data[i - 1][j], data[i][j - 1]);
                }
            }
        }

//        for(int i = 0; i < a.length() + 1; i++) {
//            for (int j = 0; j < b.length() + 1; j++) {
//                System.out.print(data[i][j] + "\t");
//            }
//            System.out.println();
//        }

        x = a.length();
        y = b.length();

        while(x > 0 && y > 0){
            if(data[x][y] == data[x - 1][y]){

                x--;

            }else if(data[x][y] == data[x][y - 1]){

                y--;
            }else{
                result = a.charAt(x - 1) + result;

                x--;
                y--;
            }
        }
        System.out.println(result.length());
        if(result.length() >= 0) {
            System.out.println(result);
        }
    }
}