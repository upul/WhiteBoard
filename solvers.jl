module Solvers

export gd

function gd(δf :: Function, X :: Matrix{Float64}, y :: Vector{Float64},
            λ :: Float64, max_iter)
  w = zeros(size(X)[2])
  for i in 1:max_iter
    Δw = δf(w, X, y)
    w = w - λ*Δw
  end
  return w
end

end
