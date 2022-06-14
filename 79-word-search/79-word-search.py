from collections import defaultdict, Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def nn(coord):
            r, c = coord
            return [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]
            
        
        letter_counts = Counter(word)
        l2rc = defaultdict(set)  # letter to row coln
        for rdx, row in enumerate(board):
            for cdx, val in enumerate(row):
                if val in letter_counts:
                    l2rc[val].add((rdx, cdx))
        
        for val, count in letter_counts.items():
            if len(l2rc[val]) < count:
                return False
        
        def dfs(pt, prev=None, visited=None) -> bool:
            
            if pt == len(word):
                return True

            l = word[pt]
            # core
            coords = l2rc[l]
            if prev is None:    
                for rc in coords:
                    visited = {rc}
                    if dfs(pt + 1, rc, visited):
                        return True
                return False
            
            nns = nn(prev)
            for rc in nns:
                if rc in coords and rc not in visited:
                    if dfs(pt + 1, rc, visited | {rc}):
                        return True
            return False
        
        
        return dfs(0)

            
            
                    
                    
            
            
            
            
            