using Microsoft.EntityFrameworkCore;
using ChurnDashboard.Models;

namespace ChurnDashboard.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

        public DbSet<ChurnData> ChurnDataSet { get; set; }
    }
}