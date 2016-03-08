emp = (('EMPNO', 'ENAME', 'JOB', 'MGR', 'HIREDATE', 'SAL', 'COMM', 'DEPTNO'),
       (7369, 'SMITH', 'CLERK', 7902, '1980-12-17 00:00:00', 800.0, 0.0, 20),
       (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20 00:00:00', 1600.0, 300.0, 30),
       (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22 00:00:00', 1250.0, 500.0, 30),
       (7566, 'JONES', 'MANAGER', 7839, '1981-04-02 00:00:00', 2975.0, 0.0, 20),
       (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28 00:00:00', 1250.0, 1400.0, 30),
       (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01 00:00:00', 2850.0, 0.0, 30),
       (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09 00:00:00', 2450.0, 0.0, 10),
       (7788, 'SCOTT', 'ANALYST', 7566, '1982-12-09 00:00:00', 3000.0, 0.0, 20),
       (7839, 'KING', 'PRESIDENT', 0, '1981-11-17 00:00:00', 5000.0, 0.0, 10),
       (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08 00:00:00', 1500.0, 0.0, 30),
       (7876, 'ADAMS', 'CLERK', 7788, '1983-01-12 00:00:00', 1100.0, 0.0, 20),
       (7900, 'JAMES', 'CLERK', 7698, '1981-12-03 00:00:00', 950.0, 0.0, 30),
       (7902, 'FORD', 'ANALYST', 7566, '1981-12-03 00:00:00', 3000.0, 0.0, 20),
       (7934, 'MILLER', 'CLERK', 7782, '1982-01-23 00:00:00', 1300.0, 0.0, 10))

dept = (('DEPTNO', 'DNAME', 'LOC'),
        (10, 'ACCOUNTING', 'NEW YORK'),
        (20, 'RESEARCH', 'DALLAS'), (30, 'SALES', 'CHICAGO'),
        (40, 'OPERATIONS', 'BOSTON'))

print emp[1::4] # Starting with the second elemnt, print every 4th element.

# select ename, sal from emp
print "\nselect ename, sal from emp: "

# select ename, sal from emp where sal > 1000
print "\nselect ename, sal from emp where sal > 1000: "

# select ename, sal from emp where sal > 1000 order by sal
print "\nselect ename, sal from emp where sal > 1000 order by sal: "

# select ename, sal from emp where sal > 1000 order by sal desc
print "\nselect ename, sal from emp where sal > 1000 order by sal desc: "

# select ename, sal from emp where sal > 1000 order by sal, ename
print "\nselect ename, sal from emp where sal > 1000 order by sal, ename: "

# select ename, sal from emp where sal > 1000 order by sal, ename desc
print "\nselect ename, sal from emp where sal > 1000 order by sal, ename desc: "

# select ename, dname from emp e join dept d on(e.deptno = d.deptno)
print "\nselect ename, dname from emp e join dept d on(e.deptno = d.deptno): "

# select deptno, avg(sal) from emp group by deptno
print "\nselect deptno, avg(sal) from emp group by deptno"

print "\nselect deptno, avg(sal) from emp group by deptno"

# select deptno, avg(sal) from emp group by deptno having avg(sal) > 2000
print "\nselect deptno, avg(sal) from emp group by deptno having avg(sal) > 2000"


# SQL: select dept.deptno, emp.ename, dept.dname from emp right outer join dept on (emp.deptno = dept.deptno)
# This just gives the cross-product of emp and dept
print "\nRight outer join step 1: "

# This eliminates all the rows where emp.deptno != dept.deptno) and adds one ( j[0], None, j[1]) tuple for each dept row (notice, this is set comprehension which eliminates duplicate ( j[0], None, j[1]) tuples)  but that's too many.
print "\nRight outer join step 2: "

# Send the list from the previous solution to a lambda function that eliminates the incorrect ( j[0], None, j[1]) tuples
print "\nRight outer join step 3: "