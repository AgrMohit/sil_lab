// DFA for all strings over {0,1} ends with 1
#define NoSt 2
#define NoIn 2
#define NoFst 1

int state[NoSt] = {0, 1};
int input[NoIn] = {0, 1};
int Rules[][NoIn] = {{0, 1}, {0, 1}};

int Final_st[NoFst] = {1};
int Initial_st = 0;