class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        int n = s.size();
        int temp = 0;
        int h[128] = {0};
        for(int i = 0;i<n;i++){
            if(h[int(s[i])] > 0)
            {
                if(h[int(s[i])] >= 2)
                for(int j = h[int(s[i])] - 2 ;j  >= (i - temp);j--){
                    h[int(s[j])] = 0;
                }
                ans = max(ans,temp);
                temp = i - h[int(s[i])]  + 1;
                h[int(s[i])] = i + 1;
            }
            else{
                temp++;
                h[int(s[i])] = i + 1;
            }
        }
        return max(ans,temp);
    }
};
