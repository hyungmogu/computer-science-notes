#include <stdio.h>
#include <stdlib.h>

void new_cmd(void);
void open_cmd(void);
void close_cmd(void);
void close_cmd(void);
void close_all_cmd(void);
void save_cmd(void);
void save_as_cmd(void);
void save_all_cmd(void);
void print_cmd(void);
void exit_cmd(void);

struct {
    char *cmd_name;
    void (*cmd_pointer)(void);
} file_cmd[] = {
    {"new", new_cmd},
    {"open", open_cmd},
    {"close", close_cmd},
    {"close all", close_all_cmd},
    {"save", save_cmd},
    {"save as", save_as_cmd},
    {"save all", save_all_cmd},
    {"print", print_cmd},
    {"exit", exit_cmd}
};

int main(void)
{
    return 0;
}


void run_cmd(const char *cmd)
{
    int cmd_cnt = sizeof(file_cmd)/sizeof(file_cmd[0]);
    char cmd_cpy[21];

    strcpy(cmd_cpy, cmd);
    if (strlen(cmd) == 21) {
        cmd_cpy[21] = '\0';
    }

    for (int i = 0; i < cmd_cnt; i++) {
        if (strcmp((file_cmd[i]).cmd_name, cmd) == 0) {
            return (file_cmd[i]).cmd_pointer();
        }
    }
}

