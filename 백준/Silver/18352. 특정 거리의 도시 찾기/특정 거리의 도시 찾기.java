package baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Queue<Integer> queue;
    static int[] visited;
    static Vector results = new Vector<>();
    static int n,k;
    static Vector[] data;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] arr = br.readLine().split(" ");
        n = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);
        k = Integer.parseInt(arr[2]);
        int x = Integer.parseInt(arr[3]);

        
        data = new Vector[n+1];
        for(int i = 0; i<=n; i++){
            data[i] = new Vector<>();
        }
        
        for(int i = 0; i<m; i++){
            String[] inputs = br.readLine().split(" ");
            int a = Integer.parseInt(inputs[0]);
            int b = Integer.parseInt(inputs[1]);
            data[a].add(b);
        }
        
        boolean isExist = bfs(x);

        if(!isExist){
            System.out.println(-1);
        }else {
            for (int i = 0; i < n + 1; i++) {
                if (visited[i] == k + 1) {
                    System.out.println(i + " ");
                }
            }
        }

        br.close();
    }
    
    public static boolean bfs(int x){
        queue = new LinkedList<>();
        visited = new int[n+1];
        visited[x] = 1;

        queue.add(x);

        boolean check = false;

        while(!queue.isEmpty()) {
            int q = queue.poll();

            for (Object tmp : data[q]) {
                int i = Integer.parseInt(tmp.toString());

                if (visited[i] == 0) {
                    visited[i] = visited[q] + 1;
                    if(visited[i] == k+1){
                        check = true;
                    }
                    queue.add(i);
                }
            }
        }
        return check;
    }
}
