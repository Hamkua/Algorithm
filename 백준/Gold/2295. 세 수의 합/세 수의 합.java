import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer[] data;
        Set<Integer> set = new HashSet<>();

        int n = Integer.parseInt(br.readLine());
        data = new Integer[n];
        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(data, Collections.reverseOrder());


        for(int x = 0; x<n; x++){
            for(int y = 0; y<n; y++){
                set.add(data[x] + data[y]);
            }
        }

        for(int k = 0; k<n; k++){
            for(int z = 0; z<n; z++){
                int tmp = data[k] - data[z];
                if(set.contains(tmp)){
                    System.out.println(data[k]);
                    br.close();
                    System.exit(0);
                }
            }
        }

        br.close();
    }
}