import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static int n;
    static int[][] data;
    static Integer[][] visited;
    static int result = Integer.MAX_VALUE;
    static Queue<Integer> queue = new LinkedList<>();    //arraylist는 queue를 상속받지 않은건가?

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int nx, ny;

    static void check(int a, int b){
        queue.add(a);
        queue.add(b);
        visited[a][b] = 0;

        while (!queue.isEmpty()){
            int x = queue.poll();
            int y = queue.poll();

            for(int i = 0; i<4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                if(0<=nx && nx<n && 0<=ny && ny<n){
                    if(data[nx][ny] == 1 && visited[nx][ny] == null){
                        visited[nx][ny] = 0;
                        queue.add(nx);
                        queue.add(ny);
                    }
                }
            }
        }
    }

    static void bfs(int a, int b){
        queue.add(a);
        queue.add(b);

        while(!queue.isEmpty()){
            int x = queue.poll();
            int y = queue.poll();

            for(int i = 0; i<4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                if(0<=nx && nx<n && 0<=ny && ny<n){
                    if(data[nx][ny] == 0 && visited[nx][ny] == null){
                        visited[nx][ny] = visited[x][y] + 1;
                        queue.add(nx);
                        queue.add(ny);
                    }else if(data[nx][ny] == 1 && visited[nx][ny] == null){
                        result = Math.min(result, visited[x][y]);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        data = new int[n][n];

        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<n; j++){
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                visited = new Integer[n][n];
                if(data[i][j] == 1 && visited[i][j] == null){
                    check(i,j);
                    if(visited[i][j] == 0){
                        bfs(i,j);
                    }
                }
            }
        }

        System.out.println(result);

        br.close();
    }
}

