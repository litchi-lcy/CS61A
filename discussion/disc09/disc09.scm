(define (fit total n)
        (define (f total n k)
            (if (and (= n 0) (= total 0))
                #t
            (if (< total (* k k))
                #f
            (or (f total-k*k (- n 1) (+ k 1)) (f total (- n 1) (+ k 1)))
            )))
        (f total n 1))

    (expect (fit 10 2) #t)  ; 1*1 + 3*3
    (expect (fit 9 1)  #t)  ; 3*3
    (expect (fit 9 2)  #f)  ;
    (expect (fit 9 3)  #f)  ; 1*1 + 2*2 + 2*2 因为重复的 2*2 所以不算
    (expect (fit 25 1)  #t) ; 5*5
    (expect (fit 25 2)  #t) ; 3*3 + 4*4