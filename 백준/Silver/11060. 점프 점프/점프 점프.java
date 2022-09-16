import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] data;
    static int[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        data = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[n];
        Arrays.fill(dp, n + 1);

//        for(int i = 0 ;i<n; i++){
//            System.out.print(dp[i] + ", ");
//        }
//        System.out.println();


        dp[0] = 0;

        for(int i = 0; i<n; i++){
            for(int j = 1; j<data[i] + 1; j++){
                if(i + j >= n){
                    break;
                }

                dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
//                for(int a = 0 ;a<n; a++){
//                    System.out.print(dp[a] + ", ");
//                }
//                System.out.println();
            }
        }

        if(dp[n - 1] >= n + 1){
            System.out.println(-1);
        }else{
            System.out.println(dp[n - 1]);
        }
    }
}