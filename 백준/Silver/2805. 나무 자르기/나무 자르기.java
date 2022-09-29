import java.util.*;
import java.io.*;

public class Main {
    static int n, m, left, right, mid;
    static long result;
    static int[] data;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }
        logic();
        System.out.println(result);


    }

    static void logic(){
        Arrays.sort(data);

        left = 0;
        result = 0;
        right = data[data.length - 1];

        while(left <= right){
            mid = (left + right) / 2;

            boolean isTrue = determination(mid);
            if(isTrue){
                result = Math.max(mid, result);
                left = mid + 1;

            }else{
                right = mid - 1;
            }
        }

    }

    static boolean determination(int h){
        long sum = 0;
        for(int i = 0; i < n; i++){
            if(h < data[i]){
                sum += (data[i] - h);
            }
        }
        return sum >= m;
    }
}
