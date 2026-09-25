using Microsoft.EntityFrameworkCore;
using ChurnDashboard.Data;

var builder = WebApplication.CreateBuilder(args);

// Adiciona os serviços MVC nativos
builder.Services.AddControllersWithViews();

// Registra a conexão com o SQL Server (Injeção do Nexus-Squad)
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

// Configura o pipeline de requisições HTTP
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();
app.UseAuthorization();

// Utiliza a otimização moderna de assets estáticos do seu SDK
app.MapStaticAssets();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")
    .WithStaticAssets();

app.Run();