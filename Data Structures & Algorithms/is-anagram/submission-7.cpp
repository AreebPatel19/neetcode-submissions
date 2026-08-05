class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        cout<<s;
        sort(t.begin(),t.end());
        cout<<t;
        if(s == t)
        {
            return true;
        }
        else
        {
            return false;
        }
        return 0;
    }
};
