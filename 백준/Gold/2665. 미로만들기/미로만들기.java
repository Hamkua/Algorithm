import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int[][] data;
    static int[][] visited;
    static Deque<Point> queue = new LinkedList<>();
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        data = new int[n][n];
        for(int i = 0; i<n; i++){
            String[] strings = br.readLine().split("");
            for(int j = 0; j<n; j++){
                data[i][j] = Integer.parseInt(strings[j]);
            }
        }

        visited = new int[n][n];
        for(int i = 0; i<n; i++) {
            Arrays.fill(visited[i], -1);
        }

        queue.add(new Point(0,0));
        visited[0][0] = 0;

        while(!queue.isEmpty()){
            Point point = queue.poll();
            int x = point.x;
            int y = point.y;

            for(int i = 0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < n){
                    if(visited[nx][ny] == -1) {
                        if (data[nx][ny] == 1) {
                            visited[nx][ny] = visited[x][y];
                            queue.addFirst(new Point(nx, ny));
                        } else if (data[nx][ny] == 0){
                            visited[nx][ny] = visited[x][y] + 1;
                            queue.addLast(new Point(nx, ny));
                        }
                    }
                }
            }
        }
        System.out.println(visited[n - 1][n - 1]);

        br.close();
    }
}