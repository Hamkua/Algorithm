import java.util.*;
import java.io.*;

public class Main {
    static int m, n, nx, ny, path;
    static int[][] data;
    static int[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        data = new int[m][n];
        visited = new int[m][n];
        for(int i = 0; i<m; i++){
            Arrays.fill(visited[i], -1);
        }


        for(int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<n; j++){
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(dfs(0,0));

    }


    public static int dfs(int x, int y){
        if(((x == m - 1) && (y == n - 1))){

            return 1;

        }else if(visited[x][y] != -1){
            return visited[x][y];

        }else{
            path = 0;
            for(int i = 0; i < 4; i++){

                nx = x + dx[i];
                ny = y + dy[i];

                if(0 <= nx && nx < m && 0 <= ny && ny < n){
                    if(data[x][y] > data[nx][ny]){
                        path += dfs(nx, ny);
                    }
                }
            }
            visited[x][y] = path;
            return path;
        }
    }
}
