import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] data;
    static int[][] visited;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        data = new int[n][m];

        visited = new int[n][m];
        for(int i = 0; i<n; i++){
            Arrays.fill(visited[i], -1);
        }

        String strings;
        for(int i = 0; i < n; i++){
            strings = br.readLine();
            for(int j = 0; j < m; j++){
                data[i][j] = strings.charAt(j) - '0';
            }
        }

        System.out.println(bfs());

    }

    public static int bfs(){
        Deque<Point> queue = new LinkedList<>();
        queue.add(new Point(0, 0));

//        Arrays.fill(visited, -1);
        visited[0][0] = 0;

        while(!queue.isEmpty()){
            Point p = queue.poll();


            for(int i = 0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m){
                    if(visited[nx][ny] == -1){
                        if(data[nx][ny] == 1){

                            queue.addLast(new Point(nx, ny));
                            visited[nx][ny] = visited[p.x][p.y] + 1;
                        }else{

                            queue.addFirst(new Point(nx, ny));
                            visited[nx][ny] = visited[p.x][p.y];
                        }
                    }
                }
            }
        }

//        for(int a = 0; a < n; a++){
//            for(int b = 0; b < m; b++){
//                System.out.print(visited[a][b] + ", ");
//            }
//            System.out.println();
//        }
        return visited[n - 1][m - 1];

    }

    static class Point{
        int x, y;
        
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}