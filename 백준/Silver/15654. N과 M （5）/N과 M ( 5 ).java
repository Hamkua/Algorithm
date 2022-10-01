import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] data;
    static LinkedList<Integer> visited = new LinkedList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        data = new int[n];

        for(int i = 0; i<n; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data);

        backtracking(0);

        System.out.print(sb);

    }

    static void backtracking(int start){

        if(visited.size() == m){
            for(int num : visited) {
                sb.append(data[num]).append(" ");
            }
            sb.append("\n");
        }else{
            for(int i = 0; i<n; i++){

                if(!visited.contains(i)) {
                    visited.add(i);
                    backtracking(i);
                    visited.pollLast();
                }
            }
        }
    }


}
