import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, searchNum, left, right;
    static StringTokenizer st;
    static int[] data;

    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        data = new int[n];
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<m; i++){
            searchNum = Integer.parseInt(st.nextToken());

            sb.append(upperBound(searchNum) - lowerBound(searchNum)).append(" ");
        }

        System.out.println(sb);

    }

    public static int upperBound(int searchNum){
        left = 0;
        right = n - 1;
        while(left <= right){
            int mid = (left + right) / 2;

            if(data[mid] > searchNum){
                right = mid - 1;
            }else if( data[mid] <= searchNum){
                left = mid + 1;
            }
        }

        return right;
    }

    public static int lowerBound(int searchNum){
        left = 0;
        right = n - 1;

        while(left <= right){
            int mid = (left + right) / 2;

            if(data[mid] >= searchNum){
                right = mid - 1;
            }else if( data[mid] < searchNum){
                left = mid + 1;
            }
        }

        return right;
    }
}
