import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int n,m;

    static int[][] graph;
    static Queue<Integer> queue = new LinkedList<>();
    public static void bfs(int r, int c){
        queue.add(r);
        queue.add(c);

        while(true){
            if(queue.isEmpty()){
                break;
            }
            int x = queue.poll();
            int y = queue.poll();
            for(int i = 0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if((0<=nx )&&(nx<n)&&(0<=ny)&&(ny<m)){
                    if(graph[nx][ny] == 1){
                        graph[nx][ny] = 0;
                        queue.add(nx);
                        queue.add(ny);
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        String[] arr = new String[2];
        for(int i = 0; i<t; i++){
            int result = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());    //세로
            n = Integer.parseInt(st.nextToken());    //가로
            int k = Integer.parseInt(st.nextToken());

            graph = new int[n][m];

            for(int j =0; j<k; j++){
                String s = br.readLine();
                arr = s.split(" ");
                int y = Integer.parseInt(arr[0]);
                int x = Integer.parseInt(arr[1]);
                graph[x][y] = 1;
            }

            for(int r = 0; r<n; r++){
                for(int c = 0; c<m; c++){
                    if(graph[r][c] == 1){
                        result++;
                        bfs(r,c);
                    }
                }
            }
            System.out.println(result);
        }
    }
}
