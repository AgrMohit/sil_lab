#include <stdio.h>

int calcwt(int n, int plist[], int bt[], int wt[])
{
  int i, sumwt;
  sumwt = 0;
  wt[0] = 0;
  for (i = 1; i <= n; i++)
    wt[i] = wt[i - 1] + bt[i - 1];

  for (i = 0; i < n; i++)
  {
    printf("pid: %d\twt: %d\n", plist[i], wt[i]);
    sumwt += wt[i];
  }
  printf("Average waiting time: %f\n", (sumwt / (float)n));
}

int calctat(int n, int plist[], int bt[], int wt[], int tat[])
{
  int i, sumtat;
  sumtat = 0;
  for (i = 0; i < n; i++)
    tat[i] = wt[i] + bt[i];
  for (i = 0; i < n; i++)
  {
    printf("pid: %d\ttat: %d\n", plist[i], tat[i]);
    sumtat += tat[i];
  }
  printf("Average turn around time: %f\n", (sumtat / (float)n));
}

int main()
{
  int i, n, plist[20], bt[20], wt[20], tat[20];

  // input section
  printf("enter number of processes: ");
  scanf("%d", &n);
  printf("Enter %d process id's in order of arrival: ", n);
  for (i = 0; i < n; i++)
    scanf("%d", &plist[i]);
  printf("Enter %d process burst times in order of arrival: ", n);
  for (i = 0; i < n; i++)
    scanf("%d", &bt[i]);

  calcwt(n, plist, bt, wt);
  calctat(n, plist, bt, wt, tat);
}