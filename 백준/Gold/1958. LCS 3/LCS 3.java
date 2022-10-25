import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static StringTokenizer st;
    static String a, b, c;
    static int aLen, bLen, cLen;
    static int[][][] data;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = br.readLine();
        b = br.readLine();
        c = br.readLine();

        aLen = a.length();
        bLen = b.length();
        cLen = c.length();

        data = new int[aLen + 1][bLen + 1][cLen + 1];
        for(int i = 0; i <= aLen; i++){
            for(int j = 0; j <= bLen; j++){
                Arrays.fill(data[i][j], 0);
            }
        }

        for(int i = 1; i <= aLen; i++){
            for(int j = 1; j <= bLen; j++){
                for(int k = 1; k <= cLen; k++){
                    if(a.charAt(i - 1) == b.charAt(j - 1) && a.charAt(i - 1) == c.charAt(k - 1)){
                        data[i][j][k] = data[i - 1][j - 1][k - 1] + 1;
                    }else{
                        data[i][j][k] = Math.max(data[i - 1][j][k], Math.max(data[i][j - 1][k], data[i][j][k - 1]));
                    }
                }
            }
        }

        System.out.println(lcs());
    }

    public static int lcs(){
        int x = aLen;
        int y = bLen;
        int z = cLen;
        int result = 0;

        while(x > 0 && y > 0 && z > 0){
            if(data[x][y][z] == data[x][y][z - 1]){
                z--;
            }else if(data[x][y][z] == data[x][y - 1][z]){
                y--;
            }else if(data[x][y][z] == data[x - 1][y][z]){
                x--;
            }else{
                result += 1;
                x--;
                y--;
                z--;
            }
        }

        return result;
    }

}
