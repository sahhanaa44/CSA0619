def orientation(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def on_segment(a,b,p):
    return min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])

def is_hull_edge(p1,p2,points):
    side=0
    for p in points:
        if p==p1 or p==p2:
            continue
        val=orientation(p1,p2,p)
        if val==0:
            if not on_segment(p1,p2,p):
                return False
            continue
        cur=1 if val>0 else -1
        if side==0:
            side=cur
        elif side!=cur:
            return False
    return True
