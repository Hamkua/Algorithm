import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] data = new int[n][m];
        int[][] visited = new int[n][m];

        for(int i = 0; i < n; i++){
            Arrays.fill(visited[i], 0);
        }

        for(int i = 0; i < n; i++){
           String s = br.readLine();
           for(int j = 0; j<m; j++){
               data[i][j] = s.charAt(j) - '0';
           }
        }

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<Point> queue = new LinkedList();

        queue.add(new Point(0, 0));
        visited[0][0] = 1;

        while(!queue.isEmpty()){
            Point point = queue.poll();

            int x = point.px;
            int y = point.py;

            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m){
                    if(data[nx][ny] != 0){
                        if(visited[nx][ny] == 0){
                            visited[nx][ny] = visited[x][y] + 1;
                            queue.add(new Point(nx, ny));
                        }
                    }
                }
            }
        }

     
        System.out.println(visited[n-1][m-1]);

    }

    static class Point{
        int px;
        int py;

        public Point(int x, int y){
            this.px = x;
            this.py = y;
        }
    }


}
