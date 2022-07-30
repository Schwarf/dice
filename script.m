GetProbabilityForNthHighestRoll[ dietype_, numberofdie_, target_, nthdie_] :=  1/dietype^numberofdie *
 Sum[ Binomial[numberofdie, i]*(
 (target - 1)^(numberofdie - i)*(dietype - target +1)^(i)-(target)^(numberofdie - i)*(dietype - target)^i), {i, nthdie, numberofdie}] /; (target - 1)