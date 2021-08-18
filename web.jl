using Dash, DashHtmlComponents, DashCoreComponents, PlotlyBase
using Pipe, DelimitedFiles, JSON

# data handling
function reader(fname, cal)
	x = readdlm(fname, String)[:, 2:end-2]
	z = zeros(size(x, 1), size(x, 2)÷2)
	for r in 1:size(x, 1)
		for c in 1:2:size(x[r, :])[1]
			z[r, Int(ceil(c/2))] = parse(Int, x[r, c+1]*x[r, c], base=16)
		end
	end
	@pipe (z[:, 1:end-8] 
		|> reshape(_', length(_)) 
		|> [_[1:3:end] _[2:3:end] _[3:3:end]]
		|> _*4.3/2^12
		|> _ .- reshape(cal, (1, 3))
		|> _/6.5e-3
	)
end

function get_data(unit)
	prefix = JSON.parsefile(unit)["FileName"]
	c = JSON.parsefile(unit)["Calibration"]
	z, dir = [0 0 0], "data"
	for f in readdir(dir)
		split(f, "_")[1] == prefix && (z = vcat(z, reader(dir*"/"*f, c)))
	end
	z
end

function make_layout()
	html_div() do
		html_h1("Data from BLE units"),
		dcc_graph(id = "u1", figure = @pipe get_data("unit1.json") |> Plot),
		dcc_graph(id = "u2", figure = @pipe get_data("unit2.json") |> Plot)
	end
end

# MAIN
# ============
app = dash()
app.layout = make_layout
run_server(app, "0.0.0.0")
