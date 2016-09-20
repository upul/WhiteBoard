#include("./solvers.jl")
using Solvers

type LinearRegression
  weights :: Vector{Float64}
end

function create(X :: Matrix{Float64}, y :: Vector{Float64},  λ :: Float64)
  X = [ones(size(y)[1])  X]
  w = Solvers.gd(δf, X, y,  λ, 10000)
  lr = LinearRegression(w)
  return lr
end

function δf(w :: Vector{Float64}, X :: Matrix{Float64}, y :: Vector{Float64})
  return -2*X'*(y -X*w)
end

function predict(model :: LinearRegression, X :: Matrix{Float64})
  X = [ones(size(X)[1]) X]
  return X*model.weights
end

##### Testing
push!(LOAD_PATH, "./solvers.jl")
X = Matrix{Float64}([12 22; 16 14; 11 19])
y = Vector{Float64}([34; 30; 30])
model = create(X, y, 0.00001)
println(model.weights)
p = predict(model, X)
println(p)
