import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Queue<Integer> queue = new LinkedList<>();
    static int n;
    static int[][] data;
    static boolean[][] visited;
    static LinkedList<Integer> result = new LinkedList<>();

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        data = new int[n][n];
        visited = new boolean[n][n];

        for(int i = 0; i<n; i++){
            String[] strings = br.readLine().split("");
            for(int j = 0; j<n; j++){
                data[i][j] = Integer.parseInt(strings[j]);
            }
        }

        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                if(!visited[i][j] && data[i][j] == 1){
                    result.add(bfs(i,j));
                }
            }
        }

        Collections.sort(result);

        System.out.println(result.size());
        for (int a: result) {
            System.out.println(a);
        }
        br.close();
    }

    static private int bfs(int x, int y){
        int count = 1;
        queue.add(x);
        queue.add(y);

        visited[x][y] = true;

        while(!queue.isEmpty()){
            int popX = queue.poll();
            int popY = queue.poll();

            for (int i = 0; i < 4 ; i++) {
                int nx = popX + dx[i];
                int ny = popY + dy[i];

                if((0 <= nx) && (nx < n) && (0 <= ny) && (ny < n)){
                    if(!visited[nx][ny] && data[nx][ny] == 1){
                        count++;
                        queue.add(nx);
                        queue.add(ny);
                        visited[nx][ny] = true;
                    }
                }
            }
        }
        return count;
    }
}
