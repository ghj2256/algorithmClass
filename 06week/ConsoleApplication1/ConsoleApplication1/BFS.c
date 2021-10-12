#include <stdio.h>
#include <stdbool.h>
#define N 9

bool visited[9];
int graph[9][3] = { {NULL}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7} };

void bfs(int x) {
	int front = -1, rear = -1;
	int queue[9] = { 0 };

	rear++;
	queue[rear] = x;

	visited[x] = 1;

	printf("%d ", x);

	while (front < rear) {
		front++;
		int n = queue[front];

		for (int d = 1; d <= N; d++) {
			if (!visited[d] && graph[n][d]) {
				rear++;
				visited[d] = 1;
				queue[rear] = d;

				printf("%d ", d);
			}
		}
	}
}

int main() {
    bfs(1);
}