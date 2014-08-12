#include <vector>
using namespace std;

//I shoudl ask interviewer is the tokens promised to be correct or not
class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        vector<int> stack;
        int a;
        int b;
        for (int i=0; i<tokens.size(); i++){
            if (stack.size() >=2){
                int a = stack.pop_back();
                int b = stack.pop_back();
            }
            if (tokens[i] == "+"){
                stack.push_back(b+a);
            }else if (tokens[i] == '-'){
                stack.push_back(b-a);
            }else if (tokens[i] == '*'){
                stack.push_back(b*a);
            }else if (tokens[i] == '/'){
                stack.push_back(b/a);
            }else{
                stack.push_back(tokens[i]);
            }
        return stack.pop_back()
        }
    }
};

int main(){
    vecter<string> tokens1 = ["2", "1", "+", "3", "*"];
    vecter<string> tokens1 = ["4", "13", "5", "/", "+"];
    vecter<string> tokens3 = ["0","3","/"];
    vecter<string> tokens4 =["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"];

    cout << evalRPN(tokens1);
    cout << evalRPN(tokens2);
    cout << evalRPN(tokens3);
    cout << evalRPN(tokens4);

}
