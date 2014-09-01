#include <vector>
#include <string>
#include <iostream>
using namespace std;

//I shoudl ask interviewer is the tokens promised to be correct or not
class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        vector<int> stack;
        int a;
        int b;
        for (unsigned i=0; i<tokens.size(); i++){
            if (stack.size() >=2){
                a = stack.back();
                stack.pop_back();
                b = stack.back();
                stack.pop_back();
            }
            if (tokens[i] == "+"){
                stack.push_back(b+a);
            }else if (tokens[i] == "-"){
                stack.push_back(b-a);
            }else if (tokens[i] == "*"){
                stack.push_back(b*a);
            }else if (tokens[i] == "/"){
                stack.push_back(b/a);
            }else{
                stack.push_back(stoi(tokens[i]));
            }
         }
        return stack.back();
    }
};

int main(){
    string tokens_1[] = {"2", "1", "+", "3", "*"};
    vector<string> tokens1(tokens_1, tokens_1 + sizeof(tokens_1)/sizeof(*tokens_1));
//    vector<string> tokens2 = ["4", "13", "5", "/", "+"];
//    vector<string> tokens3 = ["0","3","/"];
    string tokens_4[] ={"-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"};
    vector<string> tokens4(tokens_4, tokens_4 + sizeof(tokens_4)/sizeof(*tokens_4));


    Solution *solution =  new Solution;

    cout << solution->evalRPN(tokens1);
   // cout << solution->evalRPN(tokens2);
   // cout << solution->evalRPN(tokens3);
    cout << solution->evalRPN(tokens4);

}
