import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int color1;
    static int color2;
    static int color3;
    static int[][] data;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        data = new int[n][n];

        for(int i = 0; i<n; i++){
            String[] strings = br.readLine().split(" ");
            for(int j = 0; j<n; j++){
                data[i][j] = Integer.parseInt(strings[j]);
            }
        }
        cntColor(0,0,n);
        System.out.println(color1);
        System.out.println(color2);
        System.out.println(color3);
        br.close();
    }

    public static void cntColor(int a, int b, int n){
        int divIndex = n/3;

        int tmp = data[a][b];
        for(int i = a; i< (a+n); i++) {
            for (int j = b; j < (b + n); j++) {
                if (tmp != data[i][j]) {
                    for (int x = 0; x < 3; x++) {
                        for (int y = 0; y < 3; y++) {
                            cntColor(a + x * divIndex, b + y * divIndex, divIndex);
                        }
                    }
                    return;
                }
            }
        }
        if(tmp == -1){
            color1++;
        } else if(tmp == 0){
            color2++;
        } else if(tmp == 1){
            color3++;
        }
    }
}
